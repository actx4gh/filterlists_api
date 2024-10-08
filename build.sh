#!/bin/bash

# Variables
API_URL="https://api.filterlists.com/v1/openapi.json"
OUTPUT_DIR="./"
OUTPUT_FILE="openapi.json"
SERVER_URL="https://api.filterlists.com"
PACKAGE_NAME="filterlists_api"
PROJECT_NAME="filterlists-api"
PACKAGE_VERSION="$(<./version)"
LICENSE_NAME="MIT"
CONTACT_NAME="Aaron Colichia"
CONTACT_EMAIL="b72d8917-851f-4864-ad5c-61630408048d@gb4emlsep.anonaddy.com"

# Step 1: Download the OpenAPI JSON
echo "Downloading OpenAPI spec..."
curl -s "$API_URL" -o "$OUTPUT_FILE"

# Step 2: Add the server and contact information using jq
echo "Adding server and contact information..."
jq --arg url "$SERVER_URL" \
   --arg name "$CONTACT_NAME" \
   --arg email "$CONTACT_EMAIL" \
   '.servers = [{"url": $url}] | .info.contact = {"name": $name, "email": $email}' \
   "$OUTPUT_FILE" > temp.json && mv temp.json "$OUTPUT_FILE"

# Step 3: Create the configuration file for OpenAPI Generator
echo "Creating configuration file..."
cat > config.json <<EOL
{
  "packageName": "$PACKAGE_NAME",
  "projectName": "$PROJECT_NAME",
  "packageVersion": "$PACKAGE_VERSION",
  "licenseName": "$LICENSE_NAME"
}
EOL

# Step 4: Run the OpenAPI Generator to build the client
echo "Generating Python client..."
npx @openapitools/openapi-generator-cli generate \
  -i "$OUTPUT_FILE" \
  -g python \
  -o "$OUTPUT_DIR" \
  -c config.json

echo "Python client generated in $OUTPUT_DIR"

# Optional: Clean up the configuration file
rm config.json

