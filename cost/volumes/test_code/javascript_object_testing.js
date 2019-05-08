var test_obj = [
	{
		a: "1",
		b: { "x" : "alpha", "y": "beta" }
	},
	{	a: "11",
		c: "goo"}
	]
		console.log(JSON.stringify(test_obj))

			for (var i = 0; i < test_obj.length; i++) {
				//if (typeof test_obj[i]["b"] == "object") {
				if (test_obj[i]["b"]) {
					console.log("Found b; index: "+i)
				} else if (test_obj[i]["c"]) {
					console.log("Found c; index: "+i)
				} else {
					console.log("Found nothing; index: "+i)
				}
			}
