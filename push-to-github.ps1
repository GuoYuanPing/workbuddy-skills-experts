# 一键：提交本地改动并推到 GitHub（需已安装 Git，且已登录）
# 用法：
#   1. 先在网页创建空仓库，或安装 GitHub CLI 后用本脚本自动创建
#   2. 修改下方 $RepoName / $GitHubUser（或设环境变量）
#   3. 在 PowerShell 中执行:  .\push-to-github.ps1

$ErrorActionPreference = "Stop"
$env:Path = "C:\Program Files\Git\cmd;C:\Program Files\Git\bin;C:\Program Files\GitHub CLI;" + $env:Path

Set-Location $PSScriptRoot

$GitHubUser = if ($env:GITHUB_USER) { $env:GITHUB_USER } else { "YOUR_GITHUB_USERNAME" }
$RepoName   = if ($env:GITHUB_REPO) { $env:GITHUB_REPO } else { "workbuddy-skills-experts" }
$Visibility = "private"   # 建议 private；公开改成 public

if ($GitHubUser -eq "YOUR_GITHUB_USERNAME") {
    Write-Host "请先改脚本里的 `$GitHubUser，或设置环境变量 GITHUB_USER" -ForegroundColor Yellow
    exit 1
}

# 若未配置过用户信息，提示（不自动写入全局 config）
$userName = git config user.name 2>$null
$userEmail = git config user.email 2>$null
if (-not $userName -or -not $userEmail) {
    Write-Host "本仓库尚未设置 user.name / user.email。" -ForegroundColor Yellow
    Write-Host "请只对本仓库执行（示例）："
    Write-Host '  git config user.name "Tom"'
    Write-Host '  git config user.email "your@email.com"'
    exit 1
}

git add -A
$status = git status --porcelain
if (-not $status) {
    Write-Host "没有新改动需要提交。"
} else {
    git commit -m "chore: backup WorkBuddy skills and experts"
}

$remote = git remote get-url origin 2>$null
if (-not $remote) {
    $gh = Get-Command gh -ErrorAction SilentlyContinue
    if ($gh) {
        Write-Host "使用 gh 创建远程仓库 $GitHubUser/$RepoName ($Visibility) ..."
        gh auth status
        gh repo create "$GitHubUser/$RepoName" --$Visibility --source=. --remote=origin --push
        Write-Host "完成: https://github.com/$GitHubUser/$RepoName"
        exit 0
    }

    git remote add origin "https://github.com/$GitHubUser/$RepoName.git"
    Write-Host "已添加 remote。请先在 GitHub 网页新建空仓库: $RepoName（不要勾选 README）"
    Write-Host "然后执行:  git push -u origin main"
    exit 0
}

git push -u origin main
Write-Host "推送完成。"
