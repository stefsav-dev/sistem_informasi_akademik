import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:mobile/models/user_model.dart';
import '../providers/auth_provider.dart';
import '../utils/validator.dart';
import '../widgets/custom_text_field.dart';
import '../widgets/loading_button.dart';
import 'login_screen.dart';
import 'home_screen.dart';

class RegisterScreen extends ConsumerStatefulWidget {
  const RegisterScreen({super.key});

  @override
  ConsumerState<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends ConsumerState<RegisterScreen> {
  final _formKey = GlobalKey<FormState>();

  @override
  void initState() {
    super.initState();
    // Reset form saat screen dibuka
    WidgetsBinding.instance.addPostFrameCallback((_) {
      ref.read(nameProvider.notifier).state = '';
      ref.read(emailProvider.notifier).state = '';
      ref.read(passwordProvider.notifier).state = '';
      ref.read(confirmPasswordProvider.notifier).state = '';
      ref.read(errorMessageProvider.notifier).state = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    final authStatus = ref.watch(authStatusProvider);
    final errorMessage = ref.watch(errorMessageProvider);
    final name = ref.watch(nameProvider);
    final email = ref.watch(emailProvider);
    final password = ref.watch(passwordProvider);
    final confirmPassword = ref.watch(confirmPasswordProvider);
    final isPasswordVisible = ref.watch(isPasswordVisibleProvider);
    final isConfirmPasswordVisible = ref.watch(isConfirmPasswordVisibleProvider);
    
    final authService = ref.read(authProvider);

    // Auto redirect jika sudah login
    ref.listen<AuthStatus>(authStatusProvider, (previous, next) {
      if (next == AuthStatus.authenticated) {
        Navigator.of(context).pushReplacement(
          MaterialPageRoute(builder: (_) => const HomeScreen()),
        );
      }
    });

    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 20),
                
                // Header
                Center(
                  child: Column(
                    children: [
                      Container(
                        width: 80,
                        height: 80,
                        decoration: BoxDecoration(
                          color: Theme.of(context).primaryColor.withOpacity(0.1),
                          shape: BoxShape.circle,
                        ),
                        child: Icon(
                          Icons.person_add_outlined,
                          size: 40,
                          color: Theme.of(context).primaryColor,
                        ),
                      ),
                      const SizedBox(height: 24),
                      Text(
                        'Buat Akun Baru',
                        style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        'Daftar untuk memulai',
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          color: Colors.grey.shade600,
                        ),
                      ),
                    ],
                  ),
                ),
                
                const SizedBox(height: 30),

                // Error Message
                if (errorMessage != null) ...[
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.red.shade50,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.red.shade200),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.error_outline, color: Colors.red.shade700),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            errorMessage,
                            style: TextStyle(color: Colors.red.shade700),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),
                ],

                // Name Field
                CustomTextField(
                  label: 'Nama Lengkap',
                  hint: 'Masukkan nama lengkap Anda',
                  prefixIcon: Icons.person_outline,
                  provider: nameProvider,
                  validator: Validators.validateName,
                ),
                
                const SizedBox(height: 16),

                // Email Field
                CustomTextField(
                  label: 'Email',
                  hint: 'Masukkan email Anda',
                  prefixIcon: Icons.email_outlined,
                  provider: emailProvider,
                  validator: Validators.validateEmail,
                  keyboardType: TextInputType.emailAddress,
                ),
                
                const SizedBox(height: 16),

                // Password Field
                CustomTextField(
                  label: 'Password',
                  hint: 'Minimal 6 karakter',
                  prefixIcon: Icons.lock_outline,
                  obscureText: !isPasswordVisible,
                  provider: passwordProvider,
                  validator: (value) => Validators.validatePassword(value),
                  suffixIcon: IconButton(
                    icon: Icon(
                      isPasswordVisible ? Icons.visibility_off : Icons.visibility,
                    ),
                    onPressed: () {
                      ref.read(isPasswordVisibleProvider.notifier).state = 
                          !isPasswordVisible;
                    },
                  ),
                ),
                
                const SizedBox(height: 16),

                // Confirm Password Field
                CustomTextField(
                  label: 'Konfirmasi Password',
                  hint: 'Masukkan ulang password Anda',
                  prefixIcon: Icons.lock_outline,
                  obscureText: !isConfirmPasswordVisible,
                  provider: confirmPasswordProvider,
                  validator: (value) => Validators.validateConfirmPassword(
                    value, 
                    ref.read(passwordProvider)
                  ),
                  suffixIcon: IconButton(
                    icon: Icon(
                      isConfirmPasswordVisible ? Icons.visibility_off : Icons.visibility,
                    ),
                    onPressed: () {
                      ref.read(isConfirmPasswordVisibleProvider.notifier).state = 
                          !isConfirmPasswordVisible;
                    },
                  ),
                ),

                const SizedBox(height: 16),

                // Terms & Conditions
                Row(
                  children: [
                    Checkbox(
                      value: true,
                      onChanged: (value) {},
                    ),
                    Expanded(
                      child: Text(
                        'Saya setuju dengan Syarat & Ketentuan dan Kebijakan Privasi',
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey.shade600,
                        ),
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 24),

                // Register Button
                LoadingButton(
                  isLoading: authStatus == AuthStatus.loading,
                  onPressed: () {
                    if (_formKey.currentState!.validate()) {
                      authService.register(name, email, password);
                    }
                  },
                  text: 'Daftar',
                ),

                const SizedBox(height: 16),

                // Login Link
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'Sudah punya akun? ',
                      style: TextStyle(color: Colors.grey.shade600),
                    ),
                    TextButton(
                      onPressed: () {
                        Navigator.of(context).pushReplacement(
                          MaterialPageRoute(
                            builder: (_) => const LoginScreen(),
                          ),
                        );
                      },
                      child: const Text(
                        'Login',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}