def validasi_input_umur(umur):
	try:
		umur = int(umur)
		return umur if 13 <= umur <= 100 else None

		""" Sama aja kayak gini:
		if 1 <= umur <= 150:
			return umur
		
		else:
			return None
		"""

	except (ValueError, TypeError):
		return None

def validasi_input_email(email):
	return "@" in email and "." in email
