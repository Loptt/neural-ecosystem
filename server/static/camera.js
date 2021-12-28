
export class Camera {
	constructor(x, y) {
		this.x = x;
		this.y = y;
		this.absX = x;
		this.absy = y;
	}	

	transform(elements) {
		for (const e of elements) {
			e.x += this.x	
			e.y += this.y
		}

		return elements;
	}
}