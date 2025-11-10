 📸 Serverless Image/File Upload System (AWS)

This project demonstrates a fully operational, cost-optimized, and highly scalable serverless architecture for handling user file uploads from a website. The system integrates three core AWS services (API Gateway, Lambda, S3, DynamoDB) to achieve secure file handling and persistent data logging.

🔗 Live Demo & Project Status


Live Demo URL:  https://kashafkhan21.github.io/kashafkhan-aws-file-uploader/contact.html
Status: Complete & Verified (Zero Running Cost)
Architecture Serverless (Backend automatically decommissions when idle) 

🎯 Architecture and Workflow

The system is designed to upload files to highly durable storage (S3) and log the details (metadata) to a NoSQL database (DynamoDB) simultaneously, all powered by a single Python function. 

1.  Client-Side (Frontend): The user selects a file, and *JavaScript* sends the file content, encoded as *Base64*, to the secure API endpoint.
2.  Entry Point: AWS API Gateway receives the request and triggers the Lambda function.
3.  Processing: AWS Lambda (Python):
    * Decodes the Base64 file content back into binary data.
    * Uploads the raw file to the Amazon S3 bucket (s3.put_object).
    * Logs the file transaction details (*FileKey, *BucketName, *Unique ID) to the *DynamoDB* table (dynamodb.put_item).
4.  Confirmation: A successful response (statusCode: 200) is returned to the user.


***I edited the index.html file in github to give you output about successfull website and to save the cost of aws services after deleting the data in services.***

🛠 Key Technologies & Concepts
 
AWS Core: AWS Lambda, API Gateway, Amazon S3, Amazon DynamoDB, IAM Roles
Programming: Python (Boto3), JavaScript (Fetch API)
Concepts: Serverless Architecture, Base64 Encoding/Decoding, NoSQL Database Integration, Cost Optimization
