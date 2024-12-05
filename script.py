* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.about-us {
    width: 100%;
    max-width: 1200px; /* Limit max width for large screens */
    height: 100vh; /* Ensure the height fills the viewport */
    display: flex;
    flex-direction: column;
    justify-content: space-evenly; /* Space sections evenly */
    align-items: center;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.business-profile {
    text-align: center;
    margin-bottom: 15px;
}

.business-profile h1 {
    font-size: 2rem; /* Adjusted font size */
    margin-bottom: 8px;
}

.business-profile p {
    font-size: 1rem; /* Adjusted font size */
    color: #666;
    margin-bottom: 15px;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 10px; /* Reduced gap between icons */
}

.social-icon {
    text-decoration: none;
    font-size: 1rem; /* Adjusted font size */
    color: #fff;
    padding: 8px 16px;
    border-radius: 50px;
    background-color: #0078ff;
    transition: background-color 0.3s;
}

.social-icon.facebook {
    background-color: #3b5998;
}

.social-icon.instagram {
    background-color: #e4405f;
}

.social-icon:hover {
    background-color: #0056b3;
}

.pictures {
    display: flex;
    justify-content: center;
    gap: 20px; /* Reduced gap between images */
    width: 100%;
    max-width: 600px;  /* Limit width for images */
}

.profile-picture {
    width: 130px;  /* Adjusted image size */
    height: 130px;
    object-fit: cover;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

@media screen and (max-width: 768px) {
    .about-us {
        flex-direction: column;
        align-items: center;
        height: auto;
    }
    .pictures {
        flex-direction: column;
        align-items: center;
    }
    .business-profile h1 {
        font-size: 1.8rem; /* Adjusted for smaller screens */
    }
    .business-profile p {
        font-size: 0.9rem; /* Adjusted for smaller screens */
    }
    .social-links {
        gap: 8px; /* Reduced gap for smaller screens */
    }
    .social-icon {
        font-size: 0.9rem; /* Adjusted font size for smaller screens */
    }
}