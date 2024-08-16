provider "aws"{
    region = var.aws_region
}

resource "aws_s3_bucket" "example" {
  bucket = var.bucket_name
}

#Liberando acesso ao bucket
resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.example.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "example" {
  depends_on = [
    aws_s3_bucket_ownership_controls.example,
    aws_s3_bucket_public_access_block.example,
  ]

  bucket = aws_s3_bucket.example.id
  acl    = "public-read"
}

data "aws_iam_policy_document" "allow_access_from_another_account" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["123456789012"]
    }

    actions = [
      "s3:GetObject",
      "s3:ListBucket",
      "s3:PutObject"
    ]

     resources = [
      aws_s3_bucket.example.arn,
      "${aws_s3_bucket.example.arn}/*",
    ]
  }
}

#Upload do dataset
resource "aws_s3_object" "example"{
    for_each = fileset(var.path_image, "*")
    bucket = aws_s3_bucket.example.id
    acl = "public-read"
    key = each.value
    source = "${var.path_image}${each.value}"
    etag = filemd5("${var.path_image}${each.value}")

    depends_on = [aws_s3_bucket.example, aws_s3_bucket_acl.example]
}
#("C:\\Users\\Usuário\\Desktop\\ImageDataset\\${each.value}")assets\ImageDataset