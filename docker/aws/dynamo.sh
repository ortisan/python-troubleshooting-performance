#!/bin/bash
set -x
# Cria o bucket
awslocal dynamodb --endpoint-url=http://localstack:4566 create-table \
    --table-name Tick \
    --attribute-definitions \
        AttributeName=TickId,AttributeType=S \
        AttributeName=Symbol,AttributeType=S \
        AttributeName=Value,AttributeType=N \
        AttributeName=EpochTimestamp,AttributeType=N \
    --key-schema \
        AttributeName=TickId,KeyType=HASH \
        AttributeName=EpochTimestamp,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=10

set +x