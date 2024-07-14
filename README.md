# Imaging Service for DICOM Files

## Project Overview

The Imaging Service for DICOM Files is a web application built using FastAPI that handles the upload, storage, and management of DICOM files. This service supports multiple user roles (patients, technicians, doctors, admins) and provides secure access to DICOM images and metadata.

## Features

- User registration and authentication with role-based access control (patients, technicians, doctors, admins)
- Upload DICOM files and store them in a specified directory
- Extract metadata from DICOM files and store it in a PostgreSQL database
- Secure API endpoints using JWT authentication
- Dockerized application for easy deployment

## Getting Started

### Prerequisites

- Python 3.10+
- Docker
- PostgreSQL

