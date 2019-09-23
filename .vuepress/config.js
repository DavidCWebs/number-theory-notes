const pages = require('./manifest.json')

module.exports ={
	'title': 'Number Theory',
	themeConfig: {
		sidebar: [
			{
				title: 'Main Pages',
				children: pages
			}
		]
	}
}
