-- Add explicit pipeline state for swarms that are terminal but require intervention.
ALTER TYPE processing_status ADD VALUE IF NOT EXISTS 'needs_intervention';
