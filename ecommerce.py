#!/usr/bin/env python3
"""
E-commerce Portfolio Command Interpreter

This module allows interaction with an e-commerce system through
a command interpreter interface.
"""

import sys


class EcommerceSystem:
    """Class representing an e-commerce system."""

    def __init__(self):
        """Initialize the e-commerce system with an empty product list."""
        self.products = {}
        self.product_id = 1

    def list_products(self):
        """List all products available in the store."""
        if not self.products:
            print("No products available.")
            return

        for pid, details in self.products.items():
            name, price = details
            print(f"{pid}: {name} - ${price:.2f}")

    def add_product(self, name, price):
        """Add a new product to the store."""
        self.products[self.product_id] = (name, float(price))
        print(f"Product '{name}' added with ID {self.product_id}.")
        self.product_id += 1

    def remove_product(self, pid):
        """Remove a product from the store by its ID."""
        if pid in self.products:
            removed_product = self.products.pop(pid)
            print(f"Product '{removed_product[0]}' removed.")
        else:
            print(f"Product with ID {pid} not found.")

    def search_product(self, query):
        """Search for a product by name."""
        found = False
        for pid, details in self.products.items():
            name, _ = details
            if query.lower() in name.lower():
                print(f"{pid}: {name}")
                found = True
        if not found:
            print(f"No products found matching '{query}'.")


def print_help():
    """Display available commands to the user."""
    help_text = """
Available commands:
    list_products               List all products.
    add_product [name] [price]   Add a new product with name and price.
    remove_product [id]          Remove a product by its ID.
    search_product [query]       Search for products by name.
    help                        Show this help message.
    exit                        Exit the interpreter.
"""
    print(help_text)


def main():
    """Command interpreter entry point."""
    ecommerce_system = EcommerceSystem()

    while True:
        try:
            command = input("(ecom) ").strip().split()
            if not command:
                continue

            cmd = command[0]

            if cmd == "list_products":
                ecommerce_system.list_products()
            elif cmd == "add_product" and len(command) == 3:
                _, name, price = command
                ecommerce_system.add_product(name, price)
            elif cmd == "remove_product" and len(command) == 2:
                _, pid = command
                ecommerce_system.remove_product(int(pid))
            elif cmd == "search_product" and len(command) == 2:
                _, query = command
                ecommerce_system.search_product(query)
            elif cmd == "help":
                print_help()
            elif cmd == "exit":
                print("Exiting the e-commerce system.")
                sys.exit(0)
            else:
                print("Unknown command. Type 'help' for a list of commands.")
        except (ValueError, IndexError):
            print("Invalid input. Please check your command and try again.")
        except KeyboardInterrupt:
            print("\nExiting the e-commerce system.")
            sys.exit(0)


if __name__ == "__main__":
    main()

