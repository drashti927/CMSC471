# CMSC471
Version Control and Repo for Final Project

# Order Confirmation System (AWS 4-Tier Architecture)

## Overview
This project implements a serverless order confirmation system using AWS services including API Gateway, Lambda, Step Functions, DynamoDB, and S3.

## Architecture Diagram

```mermaid
graph TD
    User[User Browser] --> S3[S3 Static Frontend]
    S3 --> APIG[API Gateway]

    APIG --> L1[Lambda: Order Handler]

    L1 --> SF[Step Functions Workflow]

    subgraph Workflow
        SF --> V1[Validate Order]
        V1 --> V2[Generate Order ID]
        V2 --> V3[Store in DynamoDB]
        V3 --> V4[Save to S3 Archive]
    end

    V3 --> DDB[DynamoDB Orders]
    V4 --> S3Data[S3 Storage]

    CW[CloudWatch Monitoring] -.-> SF
    CW -.-> L1
```
