# HongCICR: circRNA Database Web Application

HongCICR is a web application designed for exploring and querying circRNA data, including information on circRNAs, their associated diseases, and functional annotations. This application provides a user-friendly interface to browse, query, and access data, along with APIs for programmatic access.

![HongCICR Logo](static/images/logo.png)

## Table of Contents

1. [Features](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#features)
2. [Project Structure](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#project-structure)
3. Getting Started
   - [Prerequisites](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#prerequisites)
   - [Setup and Installation](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#setup-and-installation)
4. Database Overview
   - [Table: circRNA_information](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#table-circrna_information)
   - [Table: circRNA_disease](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#table-circrna_disease)
   - [Table: circRNA_function](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#table-circrna_function)
5. [API Documentation](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#api-documentation)
6. [Usage Guide](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#usage-guide)
7. [License](https://chatgpt.com/c/6788c90f-0650-8008-a3ef-418b71a936e2#license)

------

## Features

- Interactive Web Interface

  :

  - View sample data from the database.
  - Query individual tables using primary keys.
  - Access database statistics.

- RESTful APIs

  :

  - Programmatic access to circRNA data, disease associations, and functional annotations.

- Easy Setup

  :

  - Lightweight Flask-based backend and a responsive frontend built with HTML, CSS, and JavaScript.

## Project Structure

```
HongCICR/
|-- app.py                # Main Flask Application
|-- templates/            # HTML templates
|   |-- index.html        # Homepage
|   |-- query.html        # Query pages
|-- static/               # Static assets
|   |-- css/
|       |-- styles.css    # CSS styling
|   |-- js/
|       |-- script.js     # JavaScript (optional)
|-- data/                 # Dataset files
|   |-- circ_info.csv
|   |-- circAtlas_disease.csv
|   |-- function_circRNA.csv
|-- requirements.txt      # Python dependencies
|-- README.md             # Project documentation
```

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

4. Place the dataset files (`circ_info.csv`, `circAtlas_disease.csv`, `function_circRNA.csv`) in the `data` directory.

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser and visit `http://127.0.0.1:5000` to access the application.

## Database Overview

### Table: circRNA_information

- **Description**: Stores basic information about circRNAs.

- Fields

  :

  - `circAtlas_ID` (TEXT): Unique identifier for the circRNA.
  - `Species` (TEXT): Name of the species.
  - `Uniform_ID` (TEXT): Unified identifier.
  - `Position` (TEXT): Genomic position of the circRNA.
  - `Strand` (TEXT): Strand direction (+/-).
  - `circRNA_type` (TEXT): Type of circRNA.
  - `MCS` (TEXT): Multiple conservation score.
  - `Tissue` (TEXT): Tissue type.
  - `Sample` (TEXT): Sample name.
  - `Length` (TEXT): Length of the circRNA in nucleotides.
  - `Sequence` (TEXT): Nucleotide sequence of the circRNA.

### Table: circRNA_disease

- **Description**: Stores associations between circRNAs and diseases.

- Fields

  :

  - `circRNA_name` (TEXT): Name of the circRNA.
  - `circAtlas_ID` (TEXT): Associated circRNA ID (foreign key).
  - `Uniform_ID` (TEXT): Unified identifier.
  - `Strand` (TEXT): Strand direction (+/-).
  - `Host_gene` (TEXT): Host gene of the circRNA.
  - `Disease_Name` (TEXT): Name of the associated disease.
  - `Expression_Pattern` (TEXT): Expression pattern.
  - `PMID` (TEXT): PubMed ID for references.
  - `miRNA` (TEXT): Associated miRNA.

### Table: circRNA_function

- **Description**: Stores functional annotations of circRNAs.

- Fields

  :

  - `circRNA_name` (TEXT): Name of the circRNA.
  - `Species` (TEXT): Name of the species.
  - `Position` (TEXT): Genomic position.
  - `Function` (TEXT): Functional description.
  - `Gene` (TEXT): Associated gene.
  - `Gene_Description` (TEXT): Description of the gene.
  - `PMID` (TEXT): PubMed ID for references.

## API Documentation

### Base URL

```
http://127.0.0.1:5000/api
```

### Endpoints

1. **GET /api/statistics**

   - **Description**: Retrieve basic statistics about the database.

   - Response

     :

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

## Usage Guide

### Accessing the Web Application

1. Launch the application by running `python app.py`.
2. Navigate to `http://127.0.0.1:5000` in your browser.
3. Use the homepage to explore sample data and access query pages.
4. Query individual tables by entering primary keys.

### Using the APIs

- Use tools like `curl`, Postman, or Python's `requests` library to interact with the API.

- Example (using 

  ```
  curl
  ```

  ):

  ```bash
  curl http://127.0.0.1:5000/api/statistics
  ```

## License

This project is open-source and available under the MIT License.