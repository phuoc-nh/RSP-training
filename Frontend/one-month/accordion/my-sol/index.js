function expand(event) {
	console.log('expand', event.target);
	const button = event.target;
	const accordionContent = button.nextElementSibling;
	console.log('>>>', accordionContent);
	accordionContent.hidden = !accordionContent.hidden;

	const icon = button.querySelector('.accordion-icon');
	icon.classList.toggle('accordion-icon--rotated')
}