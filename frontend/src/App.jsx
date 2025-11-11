import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({ title: "", description: "", price: "" });
  const [loading, setLoading] = useState(false);

  // Fetch items from Flask
  useEffect(() => {
    fetch("/items")
      .then((res) => res.json())
      .then(setItems)
      .catch((err) => console.error("Error fetching items:", err));
  }, []);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!form.title) return alert("Title is required");

    setLoading(true);
    try {
      const res = await fetch("/items", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: form.title,
          description: form.description || null,
          price: form.price ? parseFloat(form.price) : null,
        }),
      });
      if (!res.ok) throw new Error("Failed to add item");
      const newItem = await res.json();
      setItems([newItem, ...items]);
      setForm({ title: "", description: "", price: "" });
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-container">
      <h1 className="app-title">
        📦 <span>DataVault Items</span>
      </h1>

      <form className="form" onSubmit={handleSubmit}>
        <input
          name="title"
          placeholder="Title"
          value={form.title}
          onChange={handleChange}
        />
        <input
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
        />
        <input
          name="price"
          type="number"
          step="0.01"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Adding..." : "Add Item"}
        </button>
      </form>

      <div className="items-list">
        {items.map((item) => (
          <div key={item.id} className="item-card">
            <div className="item-header">
              <strong>{item.title}</strong>
              {item.price && <span>${item.price.toFixed(2)}</span>}
            </div>
            {item.description && (
              <p className="item-desc">{item.description}</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
