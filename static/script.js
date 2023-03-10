const productNameValue = productName.value;
const ingredientsValue = ingredients.value;

function validateForm() {
	const productName = document.getElementById("product-name");
	const ingredients = document.getElementById("ingredients");

	if (productName.value.trim() == "" || ingredients.value.trim() == "") {
		if (productName.value.trim() == "") {
			productName.classList.add("error");
		} else {
			productName.classList.remove("error");
		}

		if (ingredients.value.trim() == "") {
			ingredients.classList.add("error");
		} else {
			ingredients.classList.remove("error");
		}

		return false;
	} else {
		productName.classList.remove("error");
		ingredients.classList.remove("error");

		console.log("Product Name:", productNameValue);
		console.log("Ingredients:", ingredientsValue);

		return true;
	}
}

function SubmitForm(){
	if(validateForm()){
		productName.value;
		ingredients.value;
	}
}