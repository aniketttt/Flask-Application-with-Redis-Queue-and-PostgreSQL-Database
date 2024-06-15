<!DOCTYPE html>
<body>
    <h1>📋 Flask Application with Redis Queue and PostgreSQL Database</h1>

<p>
        Welcome to the Flask application that uses Redis for queuing and PostgreSQL for data storage. This project also includes an NGINX reverse proxy for managing traffic.
    </p>

<h2>🛠 Project Setup</h2>

<h3>Requirements</h3>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
    </ul>

<h3>Installation</h3>
<p>Follow these steps to set up and run the project:</p>
    <ol>
        <li>Clone this repository:</li>
        <pre><code>git clone https://github.com/aniketttt/BasicForm-with-redis-postgres.git</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd app-repo</code></pre>
        <li>Build and start the Docker containers:</li>
        <pre><code>docker-compose build
docker-compose up</code></pre>
    </ol>

<h2>🚀 Usage</h2>
<p>Once the containers are up and running, you can access the application through your web browser:</p>
    <ul>
        <li>Open <a href="http://localhost">http://localhost</a> to access the form submission page.</li>
        <li>Submit the form with your data.</li>
        <li>After submission, you will be redirected to a success page.</li>
        <li>You can view the submitted data by navigating to <a href="http://localhost/view_data">http://localhost/view_data</a>.</li>
    </ul>

<h2>📂 Project Structure</h2>
    <pre><code>.
├── Dockerfile
├── Dockerfile.worker
├── app.py
├── worker.py
├── requirements.txt
├── requirements-worker.txt
├── nginx.conf
├── templates
│   ├── index.html
│   ├── view_data.html
│   └── success.html
└── static
    └── style.css
    </code></pre>

<h2>🔧 Components</h2>
    <ul>
        <li><strong>Flask Application:</strong> Handles form submission and displays data.</li>
        <li><strong>Redis:</strong> Used as a queue for handling form submissions asynchronously.</li>
        <li><strong>PostgreSQL:</strong> Database for storing submitted data.</li>
        <li><strong>NGINX:</strong> Reverse proxy to route traffic to the Flask application.</li>
    </ul>

<h2>🐳 Docker Services</h2>
<p>The Docker Compose configuration includes the following services:</p>
    <ul>
        <li><strong>postgres:</strong> PostgreSQL database service.</li>
        <li><strong>redis:</strong> Redis queue service.</li>
        <li><strong>flask_app:</strong> Flask application service.</li>
        <li><strong>worker:</strong> Worker service that processes the Redis queue.</li>
        <li><strong>nginx:</strong> NGINX reverse proxy service.</li>
    </ul>

<h2>✍️ License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! Please feel free to submit a Pull Request.</p>
</body>
</html>
