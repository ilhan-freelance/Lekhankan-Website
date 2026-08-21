<?php
/**
 * CodeIgniter Front Controller Entry Point
 */

define('ROOTPATH', realpath(__DIR__ . '/../') . '/');
define('APPPATH', ROOTPATH . 'app/');
define('WRITABLEPATH', ROOTPATH . 'writable/');

// Load CodeIgniter Helpers
require_once APPPATH . 'Helpers/url_helper.php';
require_once APPPATH . 'Config/App.php';
require_once APPPATH . 'Config/Routes.php';
require_once APPPATH . 'Controllers/Home.php';

// Dispatch Request to Controller Route
$uri = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

// Clean leading/trailing slashes for route lookup
$routeKey = trim($uri, '/');
if ($routeKey === '' || $routeKey === 'index.php') {
    $routeKey = '/';
}

$controller = new \App\Controllers\Home();

if ($method === 'POST' && strpos($routeKey, 'contact/submit') !== false) {
    $controller->submitContact();
} else {
    $controller->index();
}
