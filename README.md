# HongCICR: circRNA Database Web Application

HongCICR is a web application designed for exploring and querying circRNA data, including information on circRNAs, their associated diseases, and functional annotations. This application provides a user-friendly interface to browse, query, and access data, along with APIs for programmatic access.

![HongCICR Logo](static/images/logo.png)

------

## Table of Contents

1. [Features](https://chatgpt.com/c/6789e77e-efc8-8009-961e-ea5a07f27d40#features)
2. [Getting Started](#Getting Started)
   - [Prerequisites](#prerequisites)
   - [Setup and Installation](#setup-and-installation)
3. [Database Overview](#Database Overview)
   - [Table: circRNA_information](#table-circrna_information)
   - [Table: circRNA_disease](#table-circrna_disease)
   - [Table: circRNA_function](#table-circrna_function)
4. [API Documentation](#api-documentation)
5. [Usage Guide](#usage-guide)
6. [License](#license)

------

## Features

- Interactive Web Interface
  - View sample data from the database.
  - Query individual tables using primary keys or species names.
  - Access database statistics.
- RESTful APIs
  - Programmatic access to circRNA data, disease associations, and functional annotations.
  - Flexible querying with parameters for specific use cases.
- Enhanced Query System
  - Query by primary IDs (e.g., circAtlas_ID) or other keys like species names.
- Responsive Design
  - Supports desktop and mobile views for better accessibility.

------

## Getting Started

### Prerequisites

Ensure the following software is installed on your system:

- **Python 3.8+**
- **pip** (Python package manager)
- **Virtualenv** (optional, for isolated environments)

### Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/HongCICR.git
   cd HongCICR
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset files from [this link](https://jbox.sjtu.edu.cn/l/y1D7o2) and place them in the `data` directory.

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser and visit `http://127.0.0.1:5000` to access the application.

------

## Database Overview

### Table: circRNA_information

| Field        | Data Type | Description                        |
| ------------ | --------- | ---------------------------------- |
| circAtlas_ID | TEXT      | Unique identifier for the circRNA  |
| Species      | TEXT      | Name of the species                |
| Uniform_ID   | TEXT      | Unified identifier                 |
| Position     | TEXT      | Genomic position of the circRNA    |
| Strand       | TEXT      | Strand direction (+/-)             |
| circRNA_type | TEXT      | Type of circRNA                    |
| MCS          | TEXT      | Multiple conservation score        |
| Tissue       | TEXT      | Tissue type                        |
| Sample       | TEXT      | Sample name                        |
| Length       | TEXT      | Length of the circRNA (nt)         |
| Sequence     | TEXT      | Nucleotide sequence of the circRNA |

### Table: circRNA_disease

| Field              | Data Type | Description                         |
| ------------------ | --------- | ----------------------------------- |
| circRNA_name       | TEXT      | Name of the circRNA                 |
| circAtlas_ID       | TEXT      | Associated circRNA ID (foreign key) |
| Uniform_ID         | TEXT      | Unified identifier                  |
| Strand             | TEXT      | Strand direction (+/-)              |
| Host_gene          | TEXT      | Host gene of the circRNA            |
| Disease_Name       | TEXT      | Name of the associated disease      |
| Expression_Pattern | TEXT      | Expression pattern                  |
| PMID               | TEXT      | PubMed ID for references            |
| miRNA              | TEXT      | Associated miRNA                    |

### Table: circRNA_function

| Field            | Data Type | Description              |
| ---------------- | --------- | ------------------------ |
| circRNA_name     | TEXT      | Name of the circRNA      |
| Species          | TEXT      | Name of the species      |
| Position         | TEXT      | Genomic position         |
| Function         | TEXT      | Functional description   |
| Gene             | TEXT      | Associated gene          |
| Gene_Description | TEXT      | Description of the gene  |
| PMID             | TEXT      | PubMed ID for references |

------

## API Documentation

### Base URL

```
http://127.0.0.1:5000/api
```

### Endpoints

1. **GET /api/statistics**

   - **Description**: Retrieve basic statistics about the database.

   - **Response**:

     ```json
     {
         "total_circRNAs": 1234,
         "total_diseases": 567,
         "total_functions": 890
     }
     ```

2. **GET /api/circRNAs**

   - **Description**: Retrieve all circRNA information.
   - **Response**: Array of circRNA records in JSON format.

3. **GET /api/diseases**

   - **Description**: Retrieve all disease associations.
   - **Response**: Array of disease association records in JSON format.

4. **GET /api/functions**

   - **Description**: Retrieve all functional annotations.
   - **Response**: Array of functional annotation records in JSON format.

5. **GET /api/query**

   - **Description**: Query specific tables using a flexible key-value parameter system.

   - **Required Parameters**:

     - `table`: The name of the table to query (e.g., `circRNA_info`, `circRNA_disease`, `circRNA_function`, `species`).
     - `key`: The search key (e.g., circAtlas_ID or species name).

   - **Example Request**:

     ```bash
     curl "http://127.0.0.1:5000/api/query?table=circRNA_info&key=hsa_circ_000056"
     ```

   - **Response**:

     ```json
     [
         {
             "circAtlas_ID": "hsa_circ_000056",
             "Species": "Homo sapiens",
             "Position": "chr5:12345-54321",
             "Strand": "+",
             ...
         }
     ]
     ```

------

## Usage Guide

### Accessing the Web Application

1. Launch the application by running `python app.py`.
2. Navigate to `http://127.0.0.1:5000` in your browser.
3. Use the homepage to explore sample data and access query pages.
4. Query individual tables by entering primary keys or species names.

### Using the APIs

- Use tools like `curl`, Postman, or Python's `requests` library to interact with the API.

- Example (using `curl`):

  ```bash
  curl http://127.0.0.1:5000/api/statistics
  ```

------

## License

This project is open-source and available under the MIT License.

