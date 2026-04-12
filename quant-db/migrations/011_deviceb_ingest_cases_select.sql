DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'pq_deviceb_ingest') THEN
    GRANT SELECT ON public.cases TO pq_deviceb_ingest;
  END IF;
END $$;
