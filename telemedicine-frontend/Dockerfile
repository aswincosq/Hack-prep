# telemedicine-frontend/Dockerfile
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the app
RUN npm run build

# Install a simple HTTP server to serve the built app
RUN npm install -g http-server

# Expose the port the app runs on
EXPOSE 8080

# Command to serve the app
CMD ["http-server", "dist"]