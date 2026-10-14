#!/usr/bin/env bash
# Usage: bash build_scan_push <app> <env> [ref]
# Dispatches build_scan_push gha workflow with app,env as inputs

WORKFLOW="build_scan_push.yml"

if [[ $# -lt 2 ]] || [[ $# -gt 3 ]]; then
  echo "Usage: $0 <app> <env> [ref]" >2
  exit 1
fi

APP=$1
ENV=$2
REF="${3:-$(git rev-parse --abbrev-ref HEAD)}"

command -v gh >/dev/null || { echo "gh CLI is required" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "Run github login first" >&2; exit 1; }

[[ "$APP" =~ ^[a-z0-9][a-z0-9-]*$ ]] || { echo "Invalid app name: $APP" >&2; exit 1; }
[[ "$ENV" =~ ^(dev|staging|prod)$ ]] || { echo "env must be dev,staging,prod"; >&2 exit 1; }

echo "Dispatching workflow $WORKFLOW for app $APP in $env environment"
gh workflow run "$WORKFLOW" --ref ref="$REF" -f app="$APP" env="$ENV"

echo "getting run id >>> "
sleep 5

RUN_ID=$(gh run list --workflow "$WORKFLOW" --branch "$REF" --limit 1 --json databaseId --jq '.[0].databaseId')
echo "Run: $(gh run view "$RUN_ID" --json url --jq .url)"
gh run watch "$RUN_ID" --exit-status
