$(document).ready(function() {
	console.log("page ready!");
	
	// on form submission ...
	$('form').on('submit', function() {
		
		console.log("the form has beeen submitted");
		
		// grab values
		var question = $('#question').html();
		var selection = $('input[name="choice"]:checked').val();
		console.log(question);
		console.log(selection);
		
		$.ajax({
			type: "POST",
			url: "/",
			data : {
				'question': question,
				'selection': selection
				},
			success: function(response) {
				console.log('ajax call was successful! response: ')
				console.log(response);
				// $('#results').html(results.total)
				// $('input').val('')
			},
			error: function(error) {
				console.log(error)
			}
		});
	});
});