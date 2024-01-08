class MyHeader extends HTMLElement
{
	connectedCallback() {
		this.innerHTML = '
			<header>
				<div class="image-container">
					<img src="pic1.jpg" alt="profile picture">
				</div>
				<nav class="top-nav">
					<ul>
						<li><a href="index.html">Home</a></li>
						<li><a href="about.html">About</a></li>
						<li><a href="career.html">Career</a></li>
						<li><a href="academy.html">The Academy</a></li>
						<li><a href="#">blog</a></li>
					</ul>
				</nav>

				<nav class="bottom-nav">
					<ul>
						<li><a href="travels.html">Travels</a></li>
						<li><a href="arts.html">Arts</a></li>
						<li><a href="sports.html">Sports</a></li>
						<li><a href="health.html">Health</a></li>
						<li><a href="contact.html">Contact</a></li>
					</ul>
				</nav>
			</header>
		'
	}
}
customElements.define('my-header', MyHeader);
