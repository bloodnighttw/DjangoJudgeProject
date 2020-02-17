
##################################################################

q1Test1 = {
	'title':"test01",
	'content':[
		"Just Test ",
		"test line2"
	],
	'visibleIO':[
		{
			'input':"input1",
			'output':"output2"
		},
		{
			'input':"input2",
			'output':"output2"
		}
	],
	'HidenIO':[
	]
}

q1Test2 = {
	'title':"[T401]數學問題",
	'content':[
		"Just Test ",
		"test line2"
	],
	'visibleIO':[
		{
			'input':"input1 \n sss",
			'output':"output2"
		},
		{
			'input':"input2",
			'output':"output2"
		}
	],
	'HidenIO':[
	]
}

##################################################################


questionRepo1 = {
	'name' : "Repo1",
	'description' : "Nothing here",
	'questions' : [q1Test1,q1Test2],
	'id' : "q1"
}


questionRepo2 = {
	'name' : "Repo2",
	'description' : 'no',
	'questions' : [q1Test1,q1Test2],
	'id' : "q2"
}


questionRepo3 = {
	'name' : "Repo3",
	'description' : 'no',
	'questions' : [q1Test1,q1Test2],
	'id' : "q3"
}

questionRepo4 = {
	'name' : "Repo4",
	'description' : "Nothing here",
	'questions' : [q1Test1,q1Test2],
	'id' : "q4"
}


repos = [
	questionRepo1,
	questionRepo2,
	questionRepo3,
	questionRepo4
]

