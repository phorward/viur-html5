# -*- coding: utf-8 -*-
from . import core as html5

class Label(html5.Label):
	def __init__(self, *args, **kwargs):
		super(Label, self).__init__(*args, **kwargs)
		self.addClass("label ignt-label")

class Input(html5.Input):
	def __init__(self, *args, **kwargs):
		super(Input, self).__init__(*args, **kwargs)
		self.addClass("input ignt-input")

class Switch(html5.Input):
	def __init__(self, *args, **kwargs):
		super(Switch, self).__init__(*args, **kwargs)

		self.addClass("switch-input")
		self["type"] = "checkbox"

class Check(html5.Input):
	def __init__(self, *args, **kwargs):
		super(Check, self).__init__(*args, **kwargs)
		self.addClass("check ignt-check")

		checkInput = html5.Input()
		checkInput.addClass("check-input")
		checkInput["type"] = "checkbox"
		self.appendChild(checkInput)

		checkLabel = html5.Label(forElem=checkInput)
		checkLabel.addClass("check-label")
		self.appendChild(checkLabel)

class Radio(html5.Div):
	def __init__(self, *args, **kwargs):
		super(Radio, self).__init__(*args, **kwargs)
		self.addClass("radio ignt-radio")

		radioInput = html5.Input()
		radioInput.addClass("radio-input")
		radioInput["type"] = "radio"
		self.appendChild(radioInput)

		radioLabel = html5.Label(forElem=radioInput)
		radioLabel.addClass("radio-label")
		self.appendChild(radioLabel)

class Select(html5.Select):
	def __init__(self, *args, **kwargs):
		super(Select, self).__init__(*args, **kwargs)
		self.addClass("select ignt-select")

		defaultOpt = html5.Option()
		defaultOpt["selected"] = True
		defaultOpt["disabled"] = True
		defaultOpt.element.innerHTML = ""
		self.appendChild(defaultOpt)

class Textarea(html5.Textarea):
	def __init__(self, *args, **kwargs):
		super(Textarea, self).__init__(*args, **kwargs)
		self.addClass("textarea ignt-textarea")

class Progress(html5.Progress):
	def __init__(self, *args, **kwargs):
		super(Progress, self).__init__(*args, **kwargs)
		self.addClass("progress ignt-progress")

class Item(html5.Div):
	def __init__(self, title=None, descr=None, className=None, *args, **kwargs):
		super(Item, self).__init__(*args, **kwargs)
		self.addClass("item ignt-item")
		if className:
			self.addClass(className)

		self.fromHTML("""
			<div class="item-image ignt-item-image" [name]="itemImage">
			</div>
			<div class="item-content ignt-item-content" [name]="itemContent">
				<div class="item-headline ignt-item-headline" [name]="itemHeadline">
				</div>
			</div>
		""")

		if title:
			self.itemHeadline.appendChild(html5.TextNode(title))

		if descr:
			self.itemSubline = html5.Div()
			self.addClass("item-subline ignt-item-subline")
			self.itemSubline.appendChild(html5.TextNode(descr))
			self.appendChild(self.itemSubline)

class Table(html5.Table):
	def __init__(self, *args, **kwargs):
		super(Table, self).__init__(*args, **kwargs)
		self.head.addClass("ignt-table-head")
		self.body.addClass("ignt-table-body")

	def prepareRow(self, row):
		assert row >= 0, "Cannot create rows with negative index"

		for child in self.body._children:
			row -= child["rowspan"]
			if row < 0:
				return

		while row >= 0:
			tableRow = html5.Tr()
			tableRow.addClass("ignt-table-body-row")
			self.body.appendChild(tableRow)
			row -= 1

	def prepareCol(self, row, col):
		assert col >= 0, "Cannot create cols with negative index"
		self.prepareRow(row)

		for rowChild in self.body._children:
			row -= rowChild["rowspan"]

			if row < 0:
				for colChild in rowChild._children:
					col -= colChild["colspan"]
					if col < 0:
						return

				while col >= 0:
					tableCell = html5.Td()
					tableCell.addClass("ignt-table-body-cell")
					rowChild.appendChild(tableCell)
					col -= 1

				return
	def fastGrid( self, rows, cols, createHidden=False ):
		colsstr = "".join(['<td class="ignt-table-body-cell"></td>' for i in range(0, cols)])
		tblstr = '<tbody [name]="body" class="ignt-table-body" >'

		for r in range(0, rows):
			tblstr += '<tr class="ignt-table-body-row %s">%s</tr>' %("is-hidden" if createHidden else "",colsstr)
		tblstr +="</tbody>"

		self.fromHTML(tblstr)