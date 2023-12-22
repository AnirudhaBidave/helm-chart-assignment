# Use an official Nginx runtime as a base image
FROM nginx:stable-alpine

# Copy the local HTML files to the default Nginx public folder
COPY ./index.html /usr/share/nginx/html/

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# Expose the port Nginx will run on
EXPOSE 80

# Command to start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
