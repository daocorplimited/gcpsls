gcloud functions deploy python-http-function \
--gen2 \
--runtime=python310 \
--region=europe-west3 \
--source=. \
--entry-point=serve_http \
--trigger-http \
--allow-unauthenticated