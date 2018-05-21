
var test_obj = [
	{
		a: "1",
		b: { "x" : "alpha", "y": "beta" }
	},
	{	a: "11",
		c: "goo"}
	]

test_obj.forEach(function(item) {
	console.log(item.a)
});
