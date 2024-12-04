def validate_json(required_fields, data):
    """Valida che tutti i campi richiesti siano presenti."""
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")

# Esempio di utilizzo:
# validate_json(["name", "email"], {"name": "John"})  # Solleva un errore
