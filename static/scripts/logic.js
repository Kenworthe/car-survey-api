/**
 * Step 1: define classes:  question, question-manager.
 * Step 2: write logic into question-manager.
 * Step 3: write logic that hits backend for more data.
 */

/**
 * question
 * 		before load: -skip conditions
 * 						- look at question manager to see previous answers
 * 						- if certain answers, skip this question.
 * 
 */

// Class
function Question(question, answers) {
	this.question = question;
	this.answers = answers;
	// function skipCondition; <-- important
}


function QuestionManager() {
	this.attributes = {
		'year' : null,
		'newFlag' : null,
		'max_passengers': null,
		'convertibleFag': null,
		'penisSize' : null
	}

	this.questions = null;


	function processNext() {

	}

	function generateAllQuestion() {
		// set this.questions to an array of Question classes.
	}


}

/**
 * new  			->  (2018 or newer);
 * 2 passengers 	->  (none);
 * convertible yes 	->  (convertible flag = true);
 * 
 */



