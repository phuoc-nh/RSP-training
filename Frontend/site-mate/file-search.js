class Entry {
	constructor(name) {
		this.name = name
	}
	isDirectory() { throw Error('Not implemented') }
}

// file
class FileEntry extends Entry {
	constructor(name, size, extension) {
		super(name)
		this.size = size
		this.extension = extension
	}

	isDirectory() {
		return false
	}
}
// folder
class FolderEntry extends Entry {
	constructor(name) {
		super(name)
		this.children = [] // list of File or folder
	}

	addChild(entry) {
		this.children.push(entry)
	}

	isDirectory() {
		return true
	}
}

class SearchParam {
	constructor(name, size, extension) {
		this.name = name
		this.size = size
		this.extension = extension
	}
}

class IFilter {
	isValid() { }
}

class NameFilter extends IFilter {
	isValid(file, params) {
		if (!params.name) {
			return true
		}

		if (file.name === params.name) {
			return true
		}

		return false
	}
}

class ExtensionFilter extends IFilter {
	isValid(file, params) {
		if (!params.extension) {
			return true
		}

		if (file.extension === params.extension) {
			return true
		}

		return false
	}
}

class MaxSizeFilter extends IFilter {
	isValid(file, params) {
		if (!params.size) {
			return true
		}

		if (file.size <= params.size) {
			return true
		}

		return false
	}
}

class Filters {
	constructor() {
		this.filters = []
		const maxSizeFilter = new MaxSizeFilter()
		const exFilter = new ExtensionFilter()
		const nameFilter = new NameFilter()

		this.filters.push(maxSizeFilter)
		this.filters.push(exFilter)
		this.filters.push(nameFilter)
	}

	isValid(file, params) {
		for (let i = 0; i < this.filters.length; i++) {
			const filter = this.filters[i];
			if (!filter.isValid(file, params)) {
				return false
			}
		}

		return true
	}
}

const root = new FolderEntry('/')
const file00 = new FileEntry('file00', 9, 'png')
const file01 = new FileEntry('file01', 999, 'jpeg')
root.addChild(file00)
root.addChild(file01)

const folder1 = new FolderEntry('folder1')
const file11 = new FileEntry('file11', 123, 'zip')
const file12 = new FileEntry('file12', 3, 'exe')
const file121 = new FileEntry('file21', 20, 'pdf')
folder1.addChild(file11)
folder1.addChild(file12)
folder1.addChild(file121)

const folder2 = new FolderEntry('folder2')
const file21 = new FileEntry('file21', 12, 'pdf')
const file22 = new FileEntry('file22', 123, 'xml')
folder2.addChild(file21)
folder2.addChild(file22)

root.addChild(folder1)
root.addChild(folder2)

console.log(root)

const fileResult = []
const params = new SearchParam('file21', 100, 'pdf')
const filters = new Filters()
// console.log('fi', filters)
// write search algorithm



function fileSearch(root, params, filters) {
	const queue = []
	queue.push(root)

	while (queue.length) {
		const entry = queue.shift()

		entry.children.forEach(el => {
			if (el.isDirectory()) {
				queue.push(el)
				return
			}
			// this is file
			if (filters.isValid(el, params)) {
				fileResult.push(el)
			}
		})
	}

	console.log('result', fileResult)
}

fileSearch(root, params, filters)




// ...existing code...

class Specification {
	isSatisfiedBy(file, params) {
		throw new Error('Not implemented');
	}
	and(other) {
		return new AndSpecification(this, other);
	}
	or(other) {
		return new OrSpecification(this, other);
	}
}

class NameSpecification extends Specification {
	isSatisfiedBy(file, params) {
		if (!params.name) return true;
		return file.name === params.name;
	}
}
class ExtensionSpecification extends Specification {
	isSatisfiedBy(file, params) {
		if (!params.extension) return true;
		return file.extension === params.extension;
	}
}
class MaxSizeSpecification extends Specification {
	isSatisfiedBy(file, params) {
		if (!params.size) return true;
		return file.size <= params.size;
	}
}
class AndSpecification extends Specification {
	constructor(left, right) {
		super();
		this.left = left;
		this.right = right;
	}
	isSatisfiedBy(file, params) {
		return this.left.isSatisfiedBy(file, params) && this.right.isSatisfiedBy(file, params);
	}
}
class OrSpecification extends Specification {
	constructor(left, right) {
		super();
		this.left = left;
		this.right = right;
	}
	isSatisfiedBy(file, params) {
		return this.left.isSatisfiedBy(file, params) || this.right.isSatisfiedBy(file, params);
	}
}

// Usage example:
const nameSpec = new NameSpecification();
const extSpec = new ExtensionSpecification();
const sizeSpec = new MaxSizeSpecification();

// Compose filters: (name AND extension) OR size
const combinedSpec = nameSpec.and(extSpec).or(sizeSpec);

function fileSearchSpec(root, params, spec) {
	const result = [];
	const queue = [root];

	while (queue.length) {
		const entry = queue.shift();
		entry.children.forEach(el => {
			if (el.isDirectory()) {
				queue.push(el);
			} else {
				if (spec.isSatisfiedBy(el, params)) {
					result.push(el);
				}
			}
		});
	}
	console.log('result', result);
	return result;
}

// Example usage:
fileSearchSpec(root, params, combinedSpec);