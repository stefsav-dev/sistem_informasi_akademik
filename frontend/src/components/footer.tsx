    "use client"

    import Link from "next/link"
    import { Button } from "@/components/ui/button"
    import { Input } from "@/components/ui/input"
    import { Separator } from "@/components/ui/separator"
    import { 
    Facebook, 
    Twitter, 
    Instagram, 
    Linkedin, 
    Github, 
    Youtube,
    Mail,
    Phone,
    MapPin,
    ArrowRight,
    Heart
    } from "lucide-react"

    export default function Footer() {
    const currentYear = new Date().getFullYear()
    
    const navigation = {
        product: [
        { name: "Features", href: "/features" },
        { name: "Pricing", href: "/pricing" },
        { name: "Integrations", href: "/integrations" },
        { name: "Enterprise", href: "/enterprise" },
        { name: "Customer Stories", href: "/stories" },
        ],
        company: [
        { name: "About Us", href: "/about" },
        { name: "Careers", href: "/careers" },
        { name: "Press", href: "/press" },
        { name: "Blog", href: "/blog" },
        { name: "Partners", href: "/partners" },
        ],
        resources: [
        { name: "Documentation", href: "/docs" },
        { name: "Help Center", href: "/help" },
        { name: "Community", href: "/community" },
        { name: "Tutorials", href: "/tutorials" },
        { name: "Support", href: "/support" },
        ],
        legal: [
        { name: "Privacy Policy", href: "/privacy" },
        { name: "Terms of Service", href: "/terms" },
        { name: "Cookie Policy", href: "/cookies" },
        { name: "Licenses", href: "/licenses" },
        { name: "Security", href: "/security" },
        ],
    }

    const socialLinks = [
        { name: "Facebook", icon: Facebook, href: "https://facebook.com", color: "hover:text-blue-600" },
        { name: "Twitter", icon: Twitter, href: "https://twitter.com", color: "hover:text-sky-500" },
        { name: "Instagram", icon: Instagram, href: "https://instagram.com", color: "hover:text-pink-600" },
        { name: "LinkedIn", icon: Linkedin, href: "https://linkedin.com", color: "hover:text-blue-700" },
        { name: "GitHub", icon: Github, href: "https://github.com", color: "hover:text-gray-900 dark:hover:text-white" },
        { name: "YouTube", icon: Youtube, href: "https://youtube.com", color: "hover:text-red-600" },
    ]

    // const contactInfo = [
    //     { icon: Mail, text: "hello@company.com", href: "mailto:hello@company.com" },
    //     { icon: Phone, text: "+1 (555) 123-4567", href: "tel:+15551234567" },
    //     { icon: MapPin, text: "123 Business Ave, Suite 100, San Francisco, CA 94105", href: "https://maps.google.com" },
    // ]

    return (
        <footer className="bg-background border-t">
        {/* Main Footer */}
        <div className="container mx-auto px-4 py-12 lg:py-16">

            {/* Links Grid */}
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-8 lg:gap-12 mb-12">
            {/* Brand Column */}
            <div className="col-span-2 md:col-span-3 lg:col-span-1">
                <Link href="/" className="inline-block mb-4">
                <span className="text-2xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                    Brand
                </span>
                </Link>
                <p className="text-sm text-muted-foreground mb-4">
                Building the future of web development with modern tools and technologies.
                </p>
                <div className="flex flex-wrap gap-3">
                {socialLinks.map((social) => (
                    <Link
                    key={social.name}
                    href={social.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`text-muted-foreground transition-colors ${social.color}`}
                    aria-label={social.name}
                    >
                    <social.icon className="h-5 w-5" />
                    </Link>
                ))}
                </div>
            </div>

            {/* Navigation Columns */}
            <div>
                <h4 className="font-semibold mb-4">Product</h4>
                <ul className="space-y-2">
                {navigation.product.map((item) => (
                    <li key={item.name}>
                    <Link 
                        href={item.href}
                        className="text-sm text-muted-foreground hover:text-foreground transition-colors"
                    >
                        {item.name}
                    </Link>
                    </li>
                ))}
                </ul>
            </div>

            <div>
                <h4 className="font-semibold mb-4">Company</h4>
                <ul className="space-y-2">
                {navigation.company.map((item) => (
                    <li key={item.name}>
                    <Link 
                        href={item.href}
                        className="text-sm text-muted-foreground hover:text-foreground transition-colors"
                    >
                        {item.name}
                    </Link>
                    </li>
                ))}
                </ul>
            </div>

            <div>
                <h4 className="font-semibold mb-4">Resources</h4>
                <ul className="space-y-2">
                {navigation.resources.map((item) => (
                    <li key={item.name}>
                    <Link 
                        href={item.href}
                        className="text-sm text-muted-foreground hover:text-foreground transition-colors"
                    >
                        {item.name}
                    </Link>
                    </li>
                ))}
                </ul>
            </div>

            <div>
                <h4 className="font-semibold mb-4">Legal</h4>
                <ul className="space-y-2">
                {navigation.legal.map((item) => (
                    <li key={item.name}>
                    <Link 
                        href={item.href}
                        className="text-sm text-muted-foreground hover:text-foreground transition-colors"
                    >
                        {item.name}
                    </Link>
                    </li>
                ))}
                </ul>
            </div>
            </div>

            <Separator className="my-8" />

            {/* Bottom Bar */}
            <div className="flex justify-center items-center">
                <div className="text-sm text-muted-foreground text-center">
                    © {currentYear} Stefanus Andre Dev
                </div>
            </div>
        </div>
        </footer>
    )
    }
