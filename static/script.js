const form = document.getElementById('url-form');
    const goodListElement = document.getElementById('good-list');
	const badListElement = document.getElementById('bad-list');
	const noteElement = document.getElementById('note');
    form.addEventListener('submit', event => {
      event.preventDefault();
      const urlInput = document.getElementById('url-input').value;
      fetch('/get_data', {
        method: 'POST',
        body: new URLSearchParams({
          'url': urlInput
        })
      })
      .then(response => response.json())
      .then(data => {
        // create an HTML string to display the data
        console.log('here is the error')
        let html = '';
        for (const [key, value] of Object.entries(data)) {
			if (key === 'good_ingredients'){
				goodListElement.innerHTML = `<p><strong>${key}:</strong> ${value}</p>`
			}
			else if (key === 'bad_ingredients'){
				badListElement.innerHTML = `<p><strong>${key}:</strong> ${value}</p>`
			}
			else if (key === 'information'){
				noteElement.innerHTML = `<p><strong>${key}:</strong> ${value}</p>`
			}
      // console.log(data['token_size'])
         // html += ;
        }
        // display the HTML string in the result element
         //= html;
      })
      .catch(error => console.error(error));
    });

// const productNameValue = productName.value;
// const ingredientsValue = ingredients.value;

// function validateForm() {
// 	const productName = document.getElementById("product-name");
// 	const ingredients = document.getElementById("ingredients");

// 	if (productName.value.trim() == "" || ingredients.value.trim() == "") {
// 		if (productName.value.trim() == "") {
// 			productName.classList.add("error");
// 		} else {
// 			productName.classList.remove("error");
// 		}

// 		if (ingredients.value.trim() == "") {
// 			ingredients.classList.add("error");
// 		} else {
// 			ingredients.classList.remove("error");
// 		}

// 		return false;
// 	} else {
// 		productName.classList.remove("error");
// 		ingredients.classList.remove("error");

// 		console.log("Product Name:", productNameValue);
// 		console.log("Ingredients:", ingredientsValue);

// 		return true;
// 	}
// }

// function SubmitForm(){
// 	if(validateForm()){
// 		productName.value;
// 		ingredients.value;
// 	}
// }
