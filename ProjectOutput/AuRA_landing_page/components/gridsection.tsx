import React from 'react';
interface GridSectionProps {
  title: string;
  gridLayout: string;
}
const GridSection: React.FC<GridSectionProps> = ({ title, gridLayout }) => {
  const gridItems = [
    { id: 1, image: 'frameworks/1.PNG', title: 'React.js', link:'https://reactjs.com' },
    { id: 2, image: 'frameworks/2.PNG', title: 'Next.js', link:'https://nextjs.com' },
    { id: 3, image: 'frameworks/3.PNG', title: 'Vue.js', link: 'https://vuejs.com' }
  ];
  return (
    <div>
      <h2 className="text-center text-3xl font-bold text-white">{title}</h2>
      <div className='flex flex-row m-4'>
        {gridItems.map((item) => (
          <div key={item.id} className="p-4 border m-4 rounded" style={{backgroundColor:'rgba(100,100,100,0.8)'}}>
            <div className="items-center justify-center">
              <a href={item.link} style={{cursor:'pointer'}}>
                <img src={item.image} alt={item.title} />
              </a>
            <a href={item.link} className="text-white" style={{textDecoration:'none', cursor:'pointer'}}>
              <h4 className="text-black">{item.title}</h4>
            </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default GridSection;
