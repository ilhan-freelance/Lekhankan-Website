<?php
/**
 * CodeIgniter URL Helper
 * Provides helper functions for base URL and asset path resolution.
 */

if (!function_exists('base_url')) {
    function base_url($path = '') {
        $protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || (isset($_SERVER['SERVER_PORT']) && $_SERVER['SERVER_PORT'] == 443)) ? "https://" : "http://";
        $host = $_SERVER['HTTP_HOST'] ?? 'localhost:8000';
        $scriptName = $_SERVER['SCRIPT_NAME'] ?? '';
        $dirName = str_replace('\\', '/', dirname($scriptName));
        $baseUrl = rtrim($protocol . $host . ($dirName !== '/' ? $dirName : ''), '/');
        
        return rtrim($baseUrl, '/') . '/' . ltrim($path, '/');
    }
}

if (!function_exists('asset_url')) {
    function asset_url($path = '') {
        return base_url($path);
    }
}
