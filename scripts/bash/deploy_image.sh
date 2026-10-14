#!/bin/bash
# Create and Push Image

set -x
set -euo pipefail

app=$1 
environment=$2
region="us-east-1"
repo="$environment/$app"

# Query ECR for app repo / fail if not found
if ! repo_uri=$( aws ecr describe-repositories \
  --region "$region" \
  --repository-names "$repo" \
  --query 'repositories[0].repositoryUri' \
  --output text 2>/dev/null); then

  echo "Error: no ECR repository named '$app' in region $region"
  exit 1  
fi

registry="${repo_uri%%/*}"

ecr_login(){
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $registry
}


scan_image(){
    image=$1
    trivy image --exit-code 1 --severity HIGH,CRITICAL --ignore-unfixed $image
}

build_image (){
    local app=${1:?app name required}
    local tag="$(date +%Y%m%d-%H%M)"
    local img_name=$app
    local env=$environment
    local platform="linux/arm64"
    local doc_root="/Library/WebServer/Documents/$app" 
    
    cd $doc_root

    docker buildx build \
      --platform "$platform" \
      --load \
      -t "$img_name" \
      "$doc_root" || return 1

    scan_image $img_name
}

push_image(){
   local img_name=$app
   local tag="$(date +%Y%m%d-%H%M)"
   local destination="$registry/$repo:$tag"

   echo "tagging image:$img_name\nwith $tag\n ...pushing to $destination"   

   #find the latest image named $img_name from docker, then tag and push
   dckrimage=$(docker image ls --filter "reference=${img_name}" --format '{{.ID}}' | head -n1)

   echo "tagging and pushing image: $dckrimage"

   docker tag $dckrimage $destination

   # For confirmation, show list of images 
   docker image ls
   ecr_login

   docker push $destination
}

build_image $1 $2
#push_image $app $environment