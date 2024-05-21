document.addEventListener('readystatechange', function() {
	document.querySelectorAll("tr.add-row").forEach(element => {
		var item = element.querySelector('a');
		item.addEventListener("click", function() {
			var checkboxes = element.previousElementSibling.previousElementSibling.querySelectorAll('input[type="checkbox"]');
			checkboxes.forEach(function(checkbox) {
                checkbox.checked = true;
	        });
		});
	});
});