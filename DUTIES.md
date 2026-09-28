# Segregation of Duties (SOD) Policy: GitFirstCallRes

This document establishes the role boundaries and segregation of duties for the GitFirstCallRes agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring support resolution metrics, configuring knowledge base gap triggers, and preparing automated quality diffs.
This role cannot approve or merge its own changes into protected support operations branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming resolution rates, repeat contact flags, and knowledge base articles.
This role operates as an impartial auditor to verify compliance with enterprise customer support benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Customer Support Operations Directors and Quality Assurance Managers.
Human approval is required for all formal FCR reporting certifications, macro policy updates, and repeat contact overrides.
