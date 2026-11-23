$csvPath = "C:\Users\samik\.gemini\antigravity\scratch\digital_payment_statistical_analysis\digital_payments_students.csv"
$data = Import-Csv $csvPath

Write-Host "=== SAMPLE BREAKDOWN ==="
Write-Host "Total sample: $($data.Count)"
$data | Group-Object Gender | ForEach-Object { "$($_.Name): $($_.Count)" }
$data | Group-Object Accommodation | ForEach-Object { "$($_.Name): $($_.Count)" }
$data | Group-Object Primary_App | ForEach-Object { "$($_.Name): $($_.Count)" }

# Daily transactions stats
$tx = $data | ForEach-Object { [int]$_.Daily_Transactions_Count }
$txMean = ($tx | Measure-Object -Average).Average
$txVar = ($tx | ForEach-Object { [Math]::Pow($_ - $txMean, 2) } | Measure-Object -Average).Average * ($tx.Count / ($tx.Count - 1))
$txSD = [Math]::Sqrt($txVar)
Write-Host "`n=== DAILY TRANSACTIONS ==="
Write-Host "Mean: $txMean"
Write-Host "Variance: $txVar"
Write-Host "StdDev: $txSD"

# Frequency table of Daily transactions
Write-Host "`n=== TX FREQUENCIES (OBSERVED) ==="
0..7 | ForEach-Object {
    $k = $_
    $cnt = ($tx | Where-Object { $_ -eq $k }).Count
    Write-Host "k=$k : count=$cnt"
}

# Spend stats
$spend = $data | ForEach-Object { [double]$_.Monthly_Digital_Spend }
$spendMean = ($spend | Measure-Object -Average).Average
$spendVar = ($spend | ForEach-Object { [Math]::Pow($_ - $spendMean, 2) } | Measure-Object -Average).Average * ($spend.Count / ($spend.Count - 1))
$spendSD = [Math]::Sqrt($spendVar)
$spendSorted = $spend | Sort-Object
$spendMedian = ($spendSorted[49] + $spendSorted[50]) / 2.0
$spendQ1 = $spendSorted[24]
$spendQ3 = $spendSorted[74]
$spendIQR = $spendQ3 - $spendQ1

Write-Host "`n=== MONTHLY SPEND STATS ==="
Write-Host "Mean: $spendMean"
Write-Host "Variance: $spendVar"
Write-Host "StdDev: $spendSD"
Write-Host "Median: $spendMedian"
Write-Host "Q1: $spendQ1, Q3: $spendQ3, IQR: $spendIQR"
Write-Host "Min: $($spendSorted[0]), Max: $($spendSorted[-1])"

# Spend by Accommodation
$hostelSpend = $data | Where-Object { $_.Accommodation -eq "Hostel" } | ForEach-Object { [double]$_.Monthly_Digital_Spend }
$daySpend = $data | Where-Object { $_.Accommodation -eq "Day Scholar" } | ForEach-Object { [double]$_.Monthly_Digital_Spend }

$n1 = $hostelSpend.Count
$m1 = ($hostelSpend | Measure-Object -Average).Average
$v1 = ($hostelSpend | ForEach-Object { [Math]::Pow($_ - $m1, 2) } | Measure-Object -Average).Average * ($n1 / ($n1 - 1))
$s1 = [Math]::Sqrt($v1)

$n2 = $daySpend.Count
$m2 = ($daySpend | Measure-Object -Average).Average
$v2 = ($daySpend | ForEach-Object { [Math]::Pow($_ - $m2, 2) } | Measure-Object -Average).Average * ($n2 / ($n2 - 1))
$s2 = [Math]::Sqrt($v2)

# Pooled variance
$sp2 = (($n1 - 1) * $v1 + ($n2 - 1) * $v2) / ($n1 + $n2 - 2)
$sp = [Math]::Sqrt($sp2)
$se = $sp * [Math]::Sqrt((1.0/$n1) + (1.0/$n2))
$tStat = ($m1 - $m2) / $se
$df = $n1 + $n2 - 2

Write-Host "`n=== TWO-SAMPLE T-TEST ==="
Write-Host "Hostel: n1=$n1, mean1=$m1, s1=$s1, var1=$v1"
Write-Host "Day Scholar: n2=$n2, mean2=$m2, s2=$s2, var2=$v2"
Write-Host "Difference (m1 - m2): $($m1 - $m2)"
Write-Host "Pooled Variance sp2: $sp2, Pooled SD sp: $sp"
Write-Host "Standard Error: $se"
Write-Host "t-statistic: $tStat (df = $df)"

# Correlation & Regression
$n = $data.Count
$sumX = 0; $sumY = 0; $sumXY = 0; $sumX2 = 0; $sumY2 = 0
for ($i = 0; $i -lt $n; $i++) {
    $xVal = $tx[$i]
    $yVal = $spend[$i]
    $sumX += $xVal
    $sumY += $yVal
    $sumXY += ($xVal * $yVal)
    $sumX2 += ($xVal * $xVal)
    $sumY2 += ($yVal * $yVal)
}
$rNumerator = ($n * $sumXY) - ($sumX * $sumY)
$rDenominator = [Math]::Sqrt((($n * $sumX2) - ($sumX * $sumX)) * (($n * $sumY2) - ($sumY * $sumY)))
$r = $rNumerator / $rDenominator
$r2 = $r * $r
$b1 = $rNumerator / (($n * $sumX2) - ($sumX * $sumX))
$b0 = ($sumY / $n) - ($b1 * ($sumX / $n))

Write-Host "`n=== CORRELATION & REGRESSION ==="
Write-Host "Pearson r: $r"
Write-Host "R-squared: $r2"
Write-Host "Slope (beta1): $b1"
Write-Host "Intercept (beta0): $b0"
Write-Host "Regression Equation: Spend = $([Math]::Round($b0, 2)) + $([Math]::Round($b1, 2)) * (Daily_Transactions)"

# Chi-Square Test: Impulse Spending vs Digital Payment Pct (>80% vs <=80%)
$cell_High_gt80 = ($data | Where-Object { $_.Impulse_Spending -eq "High" -and [double]$_.Digital_Payment_Pct -gt 80 }).Count
$cell_High_le80 = ($data | Where-Object { $_.Impulse_Spending -eq "High" -and [double]$_.Digital_Payment_Pct -le 80 }).Count
$cell_Low_gt80  = ($data | Where-Object { $_.Impulse_Spending -eq "Low" -and [double]$_.Digital_Payment_Pct -gt 80 }).Count
$cell_Low_le80  = ($data | Where-Object { $_.Impulse_Spending -eq "Low" -and [double]$_.Digital_Payment_Pct -le 80 }).Count

$rowHigh = $cell_High_gt80 + $cell_High_le80
$rowLow  = $cell_Low_gt80 + $cell_Low_le80
$colGt80 = $cell_High_gt80 + $cell_Low_gt80
$colLe80 = $cell_High_le80 + $cell_Low_le80

$e_High_gt80 = ($rowHigh * $colGt80) / [double]$n
$e_High_le80 = ($rowHigh * $colLe80) / [double]$n
$e_Low_gt80  = ($rowLow * $colGt80) / [double]$n
$e_Low_le80  = ($rowLow * $colLe80) / [double]$n

$chiSq = [Math]::Pow($cell_High_gt80 - $e_High_gt80, 2) / $e_High_gt80 +
         [Math]::Pow($cell_High_le80 - $e_High_le80, 2) / $e_High_le80 +
         [Math]::Pow($cell_Low_gt80 - $e_Low_gt80, 2) / $e_Low_gt80 +
         [Math]::Pow($cell_Low_le80 - $e_Low_le80, 2) / $e_Low_le80

Write-Host "`n=== CHI-SQUARE CONTINGENCY TABLE ==="
Write-Host "Observed: High&>80%=$cell_High_gt80, High&<=80%=$cell_High_le80 | RowTotal=$rowHigh"
Write-Host "Observed: Low&>80%=$cell_Low_gt80,  Low&<=80%=$cell_Low_le80  | RowTotal=$rowLow"
Write-Host "ColTotals: >80%=$colGt80, <=80%=$colLe80 | Total=$n"
Write-Host "Expected: E(High, >80%)=$e_High_gt80, E(High, <=80%)=$e_High_le80"
Write-Host "Expected: E(Low, >80%)=$e_Low_gt80, E(Low, <=80%)=$e_Low_le80"
Write-Host "Chi-Square Statistic: $chiSq (df = 1)"
