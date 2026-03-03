import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_riverpod/legacy.dart';
import '../models/user_model.dart';

// Provider untuk form data
final emailProvider = StateProvider<String>((ref) => '');
final passwordProvider = StateProvider<String>((ref) => '');
final nameProvider = StateProvider<String>((ref) => '');
final confirmPasswordProvider = StateProvider<String>((ref) => '');
final isPasswordVisibleProvider = StateProvider<bool>((ref) => false);
final isConfirmPasswordVisibleProvider = StateProvider<bool>((ref) => false);

// Provider untuk auth state
final authStatusProvider = StateProvider<AuthStatus>((ref) => AuthStatus.initial);
final errorMessageProvider = StateProvider<String?>((ref) => null);

// Provider untuk user data
final currentUserProvider = StateProvider<UserModel?>((ref) => null);

// Auth provider untuk fungsi login/register
final authProvider = Provider<AuthService>((ref) {
  return AuthService(ref);
});

class AuthService {
  final Ref ref;

  AuthService(this.ref);

  Future<bool> login(String email, String password) async {
    try {
      ref.read(authStatusProvider.notifier).state = AuthStatus.loading;
      ref.read(errorMessageProvider.notifier).state = null;

      // Simulasi API call
      await Future.delayed(const Duration(seconds: 2));

      // Validasi sederhana (contoh)
      if (email == 'user@example.com' && password == 'password123') {
        final user = UserModel(
          id: '1',
          name: 'John Doe',
          email: email,
          createdAt: DateTime.now(),
        );
        
        ref.read(currentUserProvider.notifier).state = user;
        ref.read(authStatusProvider.notifier).state = AuthStatus.authenticated;
        return true;
      } else {
        ref.read(errorMessageProvider.notifier).state = 'Email atau password salah';
        ref.read(authStatusProvider.notifier).state = AuthStatus.error;
        return false;
      }
    } catch (e) {
      ref.read(errorMessageProvider.notifier).state = 'Terjadi kesalahan: $e';
      ref.read(authStatusProvider.notifier).state = AuthStatus.error;
      return false;
    }
  }

  Future<bool> register(String name, String email, String password) async {
    try {
      ref.read(authStatusProvider.notifier).state = AuthStatus.loading;
      ref.read(errorMessageProvider.notifier).state = null;

      // Simulasi API call
      await Future.delayed(const Duration(seconds: 2));

      // Cek apakah email sudah terdaftar (contoh)
      if (email == 'user@example.com') {
        ref.read(errorMessageProvider.notifier).state = 'Email sudah terdaftar';
        ref.read(authStatusProvider.notifier).state = AuthStatus.error;
        return false;
      }

      // Registrasi berhasil
      final user = UserModel(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        name: name,
        email: email,
        createdAt: DateTime.now(),
      );

      ref.read(currentUserProvider.notifier).state = user;
      ref.read(authStatusProvider.notifier).state = AuthStatus.authenticated;
      return true;
    } catch (e) {
      ref.read(errorMessageProvider.notifier).state = 'Terjadi kesalahan: $e';
      ref.read(authStatusProvider.notifier).state = AuthStatus.error;
      return false;
    }
  }

  void logout() {
    ref.read(currentUserProvider.notifier).state = null;
    ref.read(authStatusProvider.notifier).state = AuthStatus.unauthenticated;
    ref.read(emailProvider.notifier).state = '';
    ref.read(passwordProvider.notifier).state = '';
    ref.read(nameProvider.notifier).state = '';
  }

  void clearError() {
    ref.read(errorMessageProvider.notifier).state = null;
  }
}