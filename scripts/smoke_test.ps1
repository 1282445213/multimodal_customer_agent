$ErrorActionPreference = "Stop"

$BaseUrl = if ($env:BASE_URL) { $env:BASE_URL.TrimEnd("/") } else { "http://127.0.0.1:8000" }
if (-not $env:KAFU_API_TOKEN) {
    throw "请先设置 KAFU_API_TOKEN"
}

$health = Invoke-RestMethod -Method Get -Uri "$BaseUrl/health"
if ($health.status -ne "ok") {
    throw "健康检查失败"
}

$headers = @{ Authorization = "Bearer $env:KAFU_API_TOKEN" }
$body = @{
    question = "椅子的扶手使用一段时间后为什么会松动？"
    session_id = "demo"
} | ConvertTo-Json
$chat = Invoke-RestMethod -Method Post -Uri "$BaseUrl/chat" -Headers $headers -ContentType "application/json" -Body $body
if ($chat.code -ne 0 -or -not $chat.data.answer) {
    throw "对话检查失败"
}

Write-Output "smoke_test=OK"
