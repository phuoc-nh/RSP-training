import { useState } from 'react';

export default function Accordion({ sections }) {
	const [openSections, setOpenSections] = useState(
		new Set(),
	);

	const expand = (value) => {
		const newSections = new Set(openSections)
		if (newSections.has(value)) {
			newSections.delete(value)
		} else {
			newSections.add(value)
		}

		setOpenSections(newSections)
	}

	return (
		<div className='accordion'>
			{sections.map(({ value, title, contents }) => {
				const isOpen = openSections.has(value)

				return (
					<div className='accordion-item'>
						<button className='accordion-item-title' onClick={() => expand(value)}>
							{title}
							<div className={`accordion-icon ${isOpen ? 'accordion-icon--rotated' : ''}`}></div>
						</button>
						{isOpen && <div className='accordion-item-contents'>
							{contents}
						</div>}
					</div>
				)
			})}
		</div>
	);
}
