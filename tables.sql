CREATE TABLE session_execution (
	id SERIAL PRIMARY KEY,
    ip VARCHAR,
    executed_at TIMESTAMP,
    machine_id INT,
    execution_log JSON
);