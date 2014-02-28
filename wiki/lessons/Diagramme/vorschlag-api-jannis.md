# Jannis Vorschlag zur Struktur der API

<svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">
	<text class="entity" x="300" y="30">Drone</text>
	<line x1="300" y1="40" x2="450" y2="140"/>
	<line x1="300" y1="40" x2="150" y2="140"/>
	<text class="entity" x="150" y="160">Transformation</text>
	<text x="300" y="160">oder</text>
	<text class="entity" x="450" y="160">Loop</text>
	<line x1="150" y1="170" x2="150" y2="270"/>
	<text class="entity" x="150" y="290">Controller</text>
	<line x1="150" y1="300" x2="150" y2="400"/>
	<line x1="150" y1="300" x2="450" y2="400"/>
	<text class="entity" x="150" y="420">Controller</text>
	<text x="300" y="420">und</text>
	<text class="entity" x="450" y="420">Upwards</text>
	<line x1="150" y1="430" x2="150" y2="530"/>
	<line x1="150" y1="430" x2="450" y2="530"/>
	<text class="entity" x="150" y="550">Rotate</text>
	<text x="300" y="550">und</text>
	<text class="entity" x="450" y="550">Randomly</text>
	<style>
		text{
			fill: black;
			text-anchor: middle;
			font-size: 16px;
			font-family: "Helvetica Neue", sans-serif;
		}
		text.entity{
			font-size: 20px;
			text-decoration: underline;
		}
		line{
			stroke: black;
			stroke-width: 1;
		}
	</style>
</svg>