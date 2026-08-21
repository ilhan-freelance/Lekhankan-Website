<?php
namespace App\Controllers;

use Config\App;

/**
 * Main Home Controller for Lekhankan Website (CodeIgniter Architecture)
 */
class Home {
    protected App $config;

    public function __construct() {
        $this->config = new App();
    }

    /**
     * Index Action: Render the main website view page.
     */
    public function index(): void {
        $data = [
            'siteName' => $this->config->siteName,
            'pageTitle' => $this->config->pageTitle,
            'metaDescription' => $this->config->metaDescription,
            'contactEmail' => $this->config->contactEmail,
            'activeSection' => 'home'
        ];

        // Load View Components (Header, Navbar, Section Partials, Footer)
        $this->renderView('pages/home', $data);
    }

    /**
     * Submit Contact Form Action: Handle contact form submissions.
     */
    public function submitContact(): void {
        header('Content-Type: application/json');

        $firstName = trim($_POST['first_name'] ?? '');
        $lastName  = trim($_POST['last_name'] ?? '');
        $email     = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
        $company   = trim($_POST['company'] ?? '');
        $service   = trim($_POST['service'] ?? '');
        $message   = trim($_POST['message'] ?? '');

        if (!$firstName || !$lastName || !$email) {
            echo json_encode([
                'status' => 'error',
                'message' => 'Please provide your first name, last name, and a valid email address.'
            ]);
            return;
        }

        // Response payload (In production: send via CI Email library / DB log)
        echo json_encode([
            'status' => 'success',
            'message' => 'Thank you, ' . htmlspecialchars($firstName) . '! Your consultation request has been received. Our team will contact you within 24 business hours.'
        ]);
    }

    /**
     * View Renderer Utility Method
     */
    protected function renderView(string $viewPath, array $data = []): void {
        extract($data);

        $viewFile = APPPATH . 'Views/' . $viewPath . '.php';
        if (file_exists($viewFile)) {
            require $viewFile;
        } else {
            echo "View file [{$viewPath}] not found.";
        }
    }
}
