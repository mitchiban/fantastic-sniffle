# The following method is an example of a method that initializes the Vertex AI SDK.

def init_sample(
    project: Optional[str] = None,
    location: Optional[str] = None,
    experiment: Optional[str] = None,
    staging_bucket: Optional[str] = None,
    credentials: Optional[google.auth.credentials.Credentials] = None,
    encryption_spec_key_name: Optional[str] = None,
    service_account: Optional[str] = None,
):

    import vertexai

    vertexai.init(
        project=project,
        location=location,
        experiment=experiment,
        staging_bucket=staging_bucket,
        credentials=credentials,
        encryption_spec_key_name=encryption_spec_key_name,
        service_account=service_account,
    )

