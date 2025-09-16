export default function ModalDialog({ children, title, open, setOpen }) {
	if (!open) return null;

	function handleOverlayClick(e) {
		console.log('e target', e.target)
		console.log('e currentTarget', e.currentTarget)
		// Only close if clicked directly on the overlay (not on modal content)
		if (e.className === e.currentTarget) {
			setOpen(false);
		}
	}

	return (
		<div className="modal-overlay" onClick={handleOverlayClick}>
			<div className="modal">
				<h1>{title}</h1>
				<div>
					{children}
				</div>
				<button onClick={() => setOpen(false)}>Close</button>
			</div>
		</div>
	);
}
