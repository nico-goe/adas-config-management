# adas-config-management
process optimization and configuration management for automotive ADAS testing

## Motivation

Modern ADAS testing involves complex configurations, frequent test iterations, and inefficient resource usage (e.g., repeated engine start cycles, redundant test setups).

This project aims to:
- Improve traceability of configurations
- Reduce redundant testing efforts
- Support reproducible test environments
- Enable more sustainable testing workflows

## Features

- Configuration structure definition
- Versioning of test setups
- Reproducible configuration states
- Basis for automation of testing workflows

## Use Case

The repository is developed in the context of a bachelor thesis focused on:
**Process optimization and sustainability in automotive testing environments**

## Architecture

The system is structured into three main components:

1. Configuration Definition  
   - Standardized format for test configurations  

2. Validation Layer  
   - Ensures required parameters and consistency  

3. Integration Layer (planned)  
   - Interface to testing pipelines and automation tools  

This modular approach enables scalability and reuse across different testing scenarios.

## Future Work

- Integration with testing pipelines
- Automated validation of configurations
- AI-supported workflow automation (e.g., using LLMs for test generation)

## Status

Work in progress – actively developed.

stay tuned

## Example Usage

```bash
python main.py validate examples/sample_config.json
